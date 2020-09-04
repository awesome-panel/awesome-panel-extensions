Split({
    columnGutters: [{
    track: 1,
    element: document.querySelector('.vertical-gutter'),
  }],
})
bodyElement = document.getElementsByTagName("body")[0]
bodyElement.onload = function(){console.log("byt");brython(1);console.log("byton")};