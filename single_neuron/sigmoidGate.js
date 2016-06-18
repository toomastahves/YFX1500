var Unit = require('./Unit');

var sigmoidGate = function() {
  this.sig = function(x) {
    return 1 / (1 + Math.exp(-x));
  };
};

sigmoidGate.prototype = {
  forward: function(u0) {
    this.u0 = u0;
    this.utop = new Unit(this.sig(this.u0.value), 0.0);
    return this.utop;
  },
  backward: function() {
    var s = this.sig(this.u0.value);
    this.u0.grad += (s * (1 - s)) * this.utop.grad;
  }
}

module.exports = sigmoidGate;
