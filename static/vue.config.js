module.exports = {
    devServer: {
        historyApiFallback: true,
        noInfo: true,
        host: '0.0.0.0',
        port: 8002,
        overlay: true,
        proxy: "http://0.0.0.0:8001"
    },
}