module.exports = {
    devServer: {
        host: '0.0.0.0',
        port: 8002,
        proxy: "http://0.0.0.0:8001"
    },
}
