function factorial(num) {
    let prod = 1
    for(let i = num; i > 0; i--) {
      prod *= i
    }
    return prod
  }
  
  module.exports = factorial;  