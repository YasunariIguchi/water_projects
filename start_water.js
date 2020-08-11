const googlehome = require('google-home-notifier');
const language = 'ja';
googlehome.device("Google-Home", language);
googlehome.ip("192.168.0.10");
googlehome.notify('水やりをします。', function(res) {
  console.log(res);
});
