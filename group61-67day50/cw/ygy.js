// 1 Easy Task) 
// შექმენი ცვლადი grade სადაც ჩაწერ მოსწავლის ნიშანს ასოების სახით:
//  A, B, C, D, F switch-მა უნდა შეამოწმოს ნიშანი და დაბეჭდოს შესაბამისი შეტყობინება:

// A — "საუკეთესო შედეგია!"

// B — "კარგია, მაგრამ მეტი შეგიძლია."

// C — "დამაკმაყოფილებელია."

// F — "სამწუხაროდ, ვერ ჩააბარე."

// default: "არასწორი ნიშანი."

// /////////////

// 2 Hard Task) შექმენი ცვლადი day სადაც მომხმარებელს შემოატანინებ რიცხვს
//  1-დან 7-ჩათვლით  თუ რიცხვი იქნება 7 ზე მაღალი ან 1 ზე დაბალი alert-ის
//   დახმარებით გამოიტანე არასწორი რიცხვი თავიდან სცადე. switch-ის გამოყენებით
//  კონსოლში გამოიტანე კვირის შესაბამისი დღე (მაგ: 1 - ორშაბათი, 7 - კვირა)

let grade = "A";

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
  alert("არასწორი რიცხვი, თავიდან სცადე.");
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

let lastName = prompt("შეიყვანე შენი გვარი");
console.log(lastName.endsWith("i") ? "გამარჯობა!" : "ნახვამდის!");



let lastName = prompt("შეიყვანე შენი გვარი");
let thirdFromEnd = lastName[lastName.length - 3];
console.log(thirdFromEnd);