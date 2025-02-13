function getMinMax(array){
    let min = Number.MAX_SAFE_INTEGER;
    let max = Number.MIN_SAFE_INTEGER;

    for (let i=0;i<array.length;i++){
        if(array[i]<min){
            min = array[i];
        }
        if(array[i]>max){
            max = array[i];
        }

    }

return {min : min, max: max};

}

let array1 = [3, 5, 4, 1, 9];
let array2 = [22, 14, 8, 17, 35, 3];

let result1 = getMinMax(array1);
console.log("Array 1: Min =", result1.min, ", Max =", result1.max);

let result2 = getMinMax(array2);
console.log("Array 2: Min =", result2.min, ", Max =", result2.max);