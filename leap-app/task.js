#!/usr/bin/env node

var leapjs = require('leapjs');
var fs = require('fs');
const {parse, stringify} = require('flatted/cjs');

var controller  = new leapjs.Controller();

controller.on('connect', function() {
  console.log("Successfully connected.");
});

controller.on('deviceConnected', function() {
  console.log("A Leap device has been connected.");
});

controller.on('deviceDisconnected', function() {
  console.log("A Leap device has been disconnected.");
});

leapjs.loop({enableGestures:true}, function(frame) {
    if (frame.hands.length > 0) {
        for (let i = 0; i < frame.hands.length; i++) {
            const hand = frame.hands[i];
            if (hand.valid) {
                fs.writeFile('message.txt', hand.roll(), (err) => {
                    if (err) throw err;
                  });    
            }        // And so on...
          }
    }
});

controller.connect();

function getType(p) {
    if (Array.isArray(p)) return 'array';
    else if (typeof p == 'string') return 'string';
    else if (p != null && typeof p == 'object') return 'object';
    else return 'other';
}
