package poke.client.comm;

import io.netty.channel.ChannelInitializer;
import io.netty.channel.ChannelPipeline;
import io.netty.channel.socket.SocketChannel;
import io.netty.handler.codec.LengthFieldBasedFrameDecoder;
import io.netty.handler.codec.LengthFieldPrepender;
import io.netty.handler.codec.compression.ZlibCodecFactory;
import io.netty.handler.codec.compression.ZlibWrapper;
import io.netty.handler.codec.protobuf.ProtobufDecoder;
import io.netty.handler.codec.protobuf.ProtobufEncoder;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import poke.comm.App;


public class CommInitializer extends ChannelInitializer<SocketChannel> {
    boolean compress = false;
    CommHandler handler;
    protected static Logger logger = LoggerFactory.getLogger("connect");
    public CommInitializer(CommHandler handler, boolean enableCompression) {
        this.handler = handler;
        this.compress = enableCompression;
    }

    @Override
    public void initChannel(SocketChannel ch) throws Exception {
        ChannelPipeline pipeline = ch.pipeline();
        logger.debug("CommInitializer - Inside initChannel");
        if (compress) {
            pipeline.addLast("deflater", ZlibCodecFactory.newZlibEncoder(ZlibWrapper.GZIP));
            pipeline.addLast("inflater", ZlibCodecFactory.newZlibDecoder(ZlibWrapper.GZIP));
        }

        /**
         * length (4 bytes).
         *
         * Note: max message size is 64 Mb = 67108864 bytes this defines a
         * framer with a max of 64 Mb message, 4 bytes are the length, and strip
         * 4 bytes
         */
        pipeline.addLast("frameDecoder", new LengthFieldBasedFrameDecoder(67108864, 0, 4, 0, 4));
        pipeline.addLast("protobufDecoder", new ProtobufDecoder(App.Request.getDefaultInstance()));
        pipeline.addLast("frameEncoder", new LengthFieldPrepender(4));
        pipeline.addLast("protobufEncoder", new ProtobufEncoder());
        pipeline.addLast("handler", handler);
    }
}