let grade = "B";

switch (grade) {
  case "A":
    console.log("საუკეთესო შედეგია!");
    break;

  case "B":
    console.log("კარგია, მაგრამ მეტი შეგიძლია.");
    break;

  case "C":
    console.log("დამაკმაყოფილებელია.");
    break;

  case "F":
    console.log("სამწუხაროდ, ვერ ჩააბარე.");
    break;

  default:
    console.log("არასწორი ნიშანი.");
}


let day = Number(prompt("შეიყვანე რიცხვი 1-დან 7-მდე"));

if (day < 1 || day > 7) {
  alert("არასწორი რიცხვი, თავიდან სცადე");
} else {
  switch (day) {
    case 1:
      console.log("ორშაბათი");
      break;
    case 2:
      console.log("სამშაბათი");
      break;
    case 3:
      console.log("ოთხშაბათი");
      break;
    case 4:
      console.log("ხუთშაბათი");
      break;
    case 5:
      console.log("პარასკევი");
      break;
    case 6:
      console.log("შაბათი");
      break;
    case 7:
      console.log("კვირა");
      break;
  }
}



let surname = prompt("შეიყვანე შენი გვარი");

surname.endsWith("i")
  ? console.log("გამარჯობა!")
  : console.log("ნახვამდის!");





  let surname = prompt("შეიყვანე შენი გვარი");

let letter = surname[surname.length - 3];

console.log(letter);