const rotate = document.getElementById("show-arrow-up")
function myFunction(x) {
    document.getElementById("pick-format__dropdown").classList.toggle("show");
        var x = rotate;
        if (rotate.style.transform === "rotate(180deg)") {
          rotate.style.transform = "rotate(0deg)";
          console.log(rotate)
        } else {
          console.log(rotate)
          rotate.style.transform = "rotate(180deg)";
        }
  }
  
  // Close the dropdown if the user clicks outside of it
  window.onclick = function(event) {
    if (!event.target.matches('.btn-download-format')) {
      var dropdowns = document.getElementsByClassName("main-content__container__download-btns__btn");
      var i;
      
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
            rotate.style.transform = 'rotate(180deg)'
          openDropdown.classList.remove('show');
          var x = rotate;
        if (rotate.style.transform === "rotate(180deg)") {
          rotate.style.transform = "rotate(0deg)";
          console.log(rotate)
        } else {
          console.log(rotate)
          rotate.style.transform = "rotate(180deg)";
        }
        }
      }
    }
  }