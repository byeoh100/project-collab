const linearSearch = (searchTerm, arr) => {
    for(let i = 0; i < arr.length; i++) {
        if(arr[i] === searchTerm) {
            return i
        }
    }
    return "Not found"
}