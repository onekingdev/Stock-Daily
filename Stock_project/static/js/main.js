// for input

document.querySelector('input[name="email"]').placeholder =
  "Enter your Email ID";
document.querySelector('input[name="email"]').classList.add("form-control");
let name_of_company = document.getElementById("id_stocks");
let li_element = name_of_company.querySelector("div");
li_element.remove();
// ul class added

document.querySelector("#id_stocks").classList.add("list-group");
document.querySelector("#id_stocks").classList.add("border-bottom");

// class added in li

let li_elements = name_of_company.querySelectorAll("div");
li_elements.forEach((el) => {
  el.classList.add("list-group-item");
});

// searching the element of li

// console.log(values_of_li);
function search() {
  let val = document.querySelector("#ser").value;
  let fil = val.toUpperCase();
  let li_value = name_of_company.querySelectorAll("div");
  for (i = 0; i < li_value.length; i++) {
    if (li_value[i].textContent.toUpperCase().indexOf(fil) > -1) {
      li_value[i].style.display = "";
    } else {
      li_value[i].style.display = "none";
    }
  }
}
document.querySelector("#sub").addEventListener("click", function () {
  document.querySelector("#ser").value = "";
  search();
});
