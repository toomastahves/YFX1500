var Unit = require('./Unit');

var multiplyGate = function() {};
multiplyGate.prototype = {
  forward: function(u0, u1) {
    this.u0 = u0;
    this.u1 = u1;
    this.utop = new Unit(u0.value * u1.value, 0.0);
    return this.utop;
  },
  backward: function() {
    this.u0.grad += this.u1.value * this.utop.grad;
    this.u1.grad += this.u0.value * this.utop.grad;
  }
}

module.exports = multiplyGate;
