function greedy_arr_sum(arr) {
    var product_arr = [];

    var product = 1;
    for(var i=0;i<arr.length;i++) {
        product_arr[i] = product;
        product *= arr[i];
    }

    var product = 1;
    for(var i=arr.length-1;i>=0;i--) {
        product_arr[i] *= product;
        product *= arr[i];
    }

    return product_arr;
}