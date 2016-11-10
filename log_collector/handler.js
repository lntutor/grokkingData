var kafkaProducer = require('./connection').kafkaProducer
var url = require('url');
// var payloads = [{ topic: 'vidsell', message: {'video_id': '123213', 'title': 'video title'}}];

module.exports = function(req, res) {
  if (!req.query || Object.keys(req.query) == 0) {
    return res.send({'ok': false, 'error': 'empty query'})
  }
  req.query['timestamp'] = Date.now()
  console.log(req.query)
  var payloads = [
        { topic: 'vidsell', messages: [JSON.stringify(req.query)] }
    ];
  kafkaProducer.send(payloads, function (err, data) {
      if (err) {
        console.log(err)
        return res.send({'ok': false, 'err': err})
      }
      return res.send({'ok': true, 'message': data})
  });
}
