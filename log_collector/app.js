process.env.TZ = 'Asia/Ho_Chi_Minh';

const express = require('express')
const bodyParser = require('body-parser')
const http = require('http')
const app = express()
const logHandler = require('./handler')

app.use(bodyParser.json())

app.get('/babydata*', logHandler)

var server = http.Server(app)

server.listen(3000, () => {
    console.log('Server started and listening at %s', 3000);
})

process.on('uncaughtException', function (error) {
    if (!error.isOperational) {
        console.log('UNCAUGHT EXCEPTION: ', error)
        process.exit(1);
    }
});

module.exports = {app: app}
