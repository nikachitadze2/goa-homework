let difficulty = "Hard";
let playerHP;

switch (difficulty) {
  case "Easy":
    playerHP = 100;
    break;
  case "Medium":
    playerHP = 70;
    break;
  case "Hard":
    playerHP = 40;
    break;
  case "Nightmare":
    playerHP = 1;
    break;
  default:
    playerHP = 50;
    console.log("სირთულე ვერ მოიძებნა არჩეულია სტანდარტული დონე");
}

console.log(playerHP);