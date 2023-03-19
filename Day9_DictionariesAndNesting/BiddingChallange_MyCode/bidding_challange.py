import art

def auction_start():
    print(art.logo)
    members = {}
    auction_inprogress = True
    while auction_inprogress:
        name = input("What is your name : \n")
        bid = int(input("What is your bid amount : \n"))
        members[name] = bid
        inprogress = input("Are there any other bidders, type 'yes' or 'no'\n").lower()
        if inprogress == 'yes':
            auction_inprogress = True
        elif inprogress == 'no':
            auction_inprogress = False
    global max
    global index
    list_members = []
    list_amounts = []
    for winner in members:
        list_members.append(winner)
    for winner in members:
        list_amounts.append(members[winner])
    max = list_amounts[0]
    index = 0
    for i in range(len(list_amounts)-1):
        if max < list_amounts[i+1]:
            max = list_amounts[i+1]
            index = i+1
    print(max)
    print(f"auction winner is {list_members[index]} and bought for : {max}")
    # if you want to skip the index you can use
#     list(members.keys())[list(members.keys()).index(max)]
auction_start()


# def find_highest_bidder(bidding_record):
#         hightest_bid = 0
#         winner = ""
#         for bidder in bidding_record:
#             bid_amount = bidding_record[bidder]
#             if bid_amount > highest_bid:
#                 highest_bid = bid_amount
#                 winner = bidder
#         print(f"The winner is {winner} with a bid of ${highest_bid}")





