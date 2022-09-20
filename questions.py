
def TopKHotelsFinder(positive_keywords, negative_keywords, hotelIds, reviews, k):
    # positive, negative keywords
    negative_keys_un = negative_keywords.split(" ")
    negative_keys = list(map(lambda x: x.lower(), negative_keys_un)) 
    positive_keys_un = positive_keywords.split(" ")
    positive_keys = list(map(lambda x: x.lower(), positive_keys_un)) 

    # create a dictionary of the hotelds to gather the costs
    hotel_dicts = {hid:0 for hid in hotelIds}
    
    # iterate through the hotelIds
    for index, id in enumerate(hotelIds):
        # if the id already placed in the dict
        if id in hotel_dicts.keys():
            new_review_processed_dups = reviews[index].split(" ")
            for word in new_review_processed_dups:
                if ',' in word:
                    word = word.rstrip(',')
                elif '.' in word:
                    word = word.rstrip('.')
                else:
                    if word.lower() in positive_keys:
                        hotel_dicts[id] += 3
                    elif word.lower() in negative_keys:
                        hotel_dicts[id] -= 1

    result = sorted(hotel_dicts.items(), key=lambda item: item[1], reverse=True)
    return [result[0][0], result[1][0]]
    
if __name__ == "__main__":
    # test case
    positive_keywords = "breakfast beach city center location metro view staff price"
    negative_keywords = "not"
    m = 5 # number of hotelids
    hotelIds = [1, 2, 1, 1, 2]
    n = 5 # hotel reviews
    reviews = ["This hotel has a nice view of the city center. The location is perfect.",
    "The breakfast is ok. Regarding location, it is quite far from the city center but price is cheap so it is worth it.",
    "Location is excellent, 5 minutes from the city center. There is also a metro station very close to the hotel.",
    "They said I couldn't take my dog and there were other guests with dogs! That is not fair.",
    "Very friendly staff and a good cost-benefit ratio. Its location is a bit far from the city center."]
    k = 2

    # return the k top hotels
    topTwo = TopKHotelsFinder(positive_keywords, negative_keywords, hotelIds, reviews, k)
    print(topTwo)