const btn = document.querySelector('.view-more-cards')
const batchTwo = document.querySelector('.batch-two')
const handleViewMore = () => {
    if(batchTwo.style.display == "flex"){
        batchTwo.style.display = "none"
    } else{
        batchTwo.style.display = "flex"
    }
}


btn.addEventListener("click", handleViewMore)