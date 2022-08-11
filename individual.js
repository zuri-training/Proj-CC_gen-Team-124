const rotate = document.getElementById("show-arrow-up");
function myFunction(x) {
  document.getElementById("pick-format__dropdown").classList.toggle("show");
  var x = rotate;
  if (rotate.style.transform === "rotate(180deg)") {
    rotate.style.transform = "rotate(0deg)";
    console.log(rotate);
  } else {
    console.log(rotate);
    rotate.style.transform = "rotate(180deg)";
  }
}

// Close the dropdown if the user clicks outside of it
window.onclick = function (event) {
  if (!event.target.matches(".btn-download-format")) {
    var dropdowns = document.getElementsByClassName(
      "main-content__container__download-btns__btn"
    );
    var i;

    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains("show")) {
        rotate.style.transform = "rotate(180deg)";
        openDropdown.classList.remove("show");
        var x = rotate;
        if (rotate.style.transform === "rotate(180deg)") {
          rotate.style.transform = "rotate(0deg)";
          console.log(rotate);
        } else {
          console.log(rotate);
          rotate.style.transform = "rotate(180deg)";
        }
      }
    }
  }
};

// Comment Overlay
const commentModal = document.getElementById("commentModal");
const openCommentModal = document.getElementById("openCommentModal");
const closeCommentModal = document.getElementById("closeCommentModal");

openCommentModal.addEventListener("click", () => {
  commentModal.classList.add("showCommentModal");
});

closeCommentModal.addEventListener("click", () => {
  commentModal.classList.remove("showCommentModal");
});

console.log(commentModal, openCommentModal, closeCommentModal);

window.addEventListener("click", (event) => {
  if (event.target === commentModal) {
    commentModal.classList.remove("showCommentModal");
  }
});


// Share overlay - copy link
const cardLinkInput = document.getElementById('card-link');
const copyCardLinkBtn = document.getElementById('card-link-btn');

const copyLinkToClipboard = async () => {
  await navigator.clipboard.writeText(cardLinkInput.value);
}

copyCardLinkBtn.addEventListener('click', copyLinkToClipboard);

const shareBtn = document.getElementById('share-btn');

const shareModal = document.getElementById('share-container');
const shareModalCloseBtn = document.getElementById('share-modal-close-btn');

shareBtn.addEventListener('click', () => shareModal.classList.add('share-con--show'));
shareModalCloseBtn.addEventListener('click', () => shareModal.classList.remove('share-con--show'));

document.body.addEventListener("click", (event) => {
  if (event.target.id == 'share-container') {
    shareModal.classList.remove("share-con--show");
  }
});