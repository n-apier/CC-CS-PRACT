const _ = { 
    clamp(num, low, high){
        lowerClampedValue = Math.max(num, low);
        clampedValue = Math.min(lowerClampedValue, high);
      return clampedValue;
      },
    
    inRange(num, start, end){
        if (end === undefined){
            end = start;
            start = 0;
          }
        if ( start > end ) {
            var temp = end;
            end = start;
            start = temp;
          }
      var isInRange = ( start <= num && num < end );
      return isInRange;
      },
    
    words(string){
      words = string.split(' ');
      return words;
      },
    
    pad(string, length){
      if (length <= string.length){
        return string;
      }
    
      let startPaddingLength = Math.floor( (length - string.length ) / 2);
      let endPaddingLength = (length - string.length - startPaddingLength);
    
      let paddedString = ' '.repeat(startPaddingLength) + string + ' '.repeat(endPaddingLength);
    
      return paddedString;
      },
    has(object, key){
      let hasValue = object.hasOwnProperty(key) ? (object[key] ? true:false) : false;
      return hasValue;
      },
    invert(object){
    
      let inverted = {};
    
      for(key in object){
      inverted[object[key]] = key;
      }
      return inverted;
      },
    
    findKey(object, predicate){
        for(key in object){
          let value = object[key];
          let predicateReturnValue = predicate(value);
          if (predicateReturnValue){
            return key;
          }
          return undefined;
        }
      },
    
    drop(array, n = 1){
        return array.slice(n);
      },
    dropWhile(array, predicate){
        const cb = (element, index) => {
          return !predicate(element, index, array);
        };
        // above is an anon. function 
        let dropNumber = array.findIndex(cb);
        let droppedArray = this.drop(array, dropNumber);
        return droppedArray;
      },
    
    chunk(array, size = 1){
      let arrayChunks = [];
        for(let i = 0; i < array.length; i += size){
          let arrayChunk = array.slice(i, i+size);
          arrayChunks.push(arrayChunk);
        }
        return arrayChunks;
    }
    
    };
    
    
    
    // Do not write or modify code below this line.
    module.exports = _;