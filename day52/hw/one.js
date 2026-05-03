let cartTotal = 120;
let deliveryFee;

switch (true) {
  case cartTotal > 100:
    deliveryFee = 0;
    break;
  default:
    deliveryFee = 10;
}

console.log(deliveryFee);