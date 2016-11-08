
var kafka = require('kafka-node')
var Producer = kafka.Producer
var client = new kafka.Client('61.28.227.194:2181,61.28.227.200:2181')
var kafkaProducer = new Producer(client);

kafkaProducer.on('ready', function () {
  console.log('successfully init kafka producer')
});

kafkaProducer.on('error', function (err) {
  console.log(err)
  process.exit(1)
})

module.exports.kafkaProducer = kafkaProducer
