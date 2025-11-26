students_scores = {
    "გიორგი": 85,
    "ნინო": 92,
    "ლაშა": 78,
    "მარიამი": 95,
    "დათო": 88
}

best = max(students_scores, key=students_scores.get)
print(best, students_scores[best])



productprice = {
    "პური": 1.2,
    "რძე": 2.5,
    "ყველი": 5.0,
    "კვერცხი": 3.0
}

total_price = sum(productprice.values())
print("პროდუქტების ჯამური ფასი: {total_price} ლარი")

books = {"ოსტატი და მარგარიტა": "მიხაილ ბულგაკოვი", 
         "დედა": "მაქსიმ გორკი", 
         "ვეფხისტყაოსანი": "შოთა რუსთაველი", 
         "კაპიტან გრანტის შვილები": "ჟიულ ვერნი"
         }
print("წიგნის 'ვეფხისტყაოსანი' ავტორია: {books.get('ვეფხისტყაოსანი','ავტორი ვერ მოიძებნა')}")