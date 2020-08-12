const googlehome = require('google-home-notifier');
const language = 'ja';
googlehome.device("Google-Home", language);
googlehome.ip("192.168.0.30");
googlehome.notify('水やりが終わりました。', function(res) {
  console.log(res);
});
