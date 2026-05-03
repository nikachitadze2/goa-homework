let choice = Number(prompt("აირჩიე: 1-ბალანსი 2-შეტანა 3-გატანა"));

switch (choice) {
  case 1:
    console.log("ბალანსის ნახვა");
    break;
  case 2:
    console.log("თანხის შეტანა");
    break;
  case 3:
    console.log("თანხის გატანა");
    break;
  default:
    console.log("არასწორი არჩევანი");
}