function showSecondaryAddress() {
    console.log("Secondary address Checkbox clicked!");
    var checkbox = document.getElementById("secondary-address-checkbox");
    var secondaryAddress = document.getElementById("secondary-address");
    checkbox.addEventListener("change", function() {
    if (checkbox.checked) {
      secondaryAddress.style.display = "block";
    } else {
      secondaryAddress.style.display = "none";
    }
  })
}