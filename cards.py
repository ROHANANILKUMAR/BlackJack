def load_cards():
    symbols=["diamond","spade","heart","clubs"]
    numbers=["A","1","2","3","4","5","6","7","8","9","10","J","K","Q"]
    result=[]
    for i in symbols:
        for m in numbers:
            result.append(i+" "+m)
    return result

def read_value(cards):
    result=0
    for i in cards:
        if i[-1] in ["J","K","Q"]:
            result += 10
        elif i[0] == "A":
            return "Err"
        elif len(i)==1:
            result+=1
        elif len(i)==2:
            result+=11
        elif "10" in i:
            result += 10
        else:
            result += int(i[-1])
    return result

def card_grapics(card,i):
    symbols={"club": "♣", "diamond" : "♦", "heart" : "♥", "spade" : "♠"}
    card_graph=f"""{i}+---------+
{i}| x       |
{i}|         |
{i}|    y    |
{i}|         |
{i}|       x |
{i}+---------+"""
    if "10" in card:
        if "club" in card:
            return card_graph.replace("x ","10").replace("y",symbols["club"])
        elif "diamond" in card:
            return card_graph.replace("x ","10").replace("y",symbols["diamond"])
        elif "heart" in card:
            return card_graph.replace("x ","10").replace("y",symbols["heart"])
        elif "spade" in card:
            return card_graph.replace("x ","10").replace("y",symbols["spade"])
    elif "club" in card:
        return card_graph.replace("x",card[-1]).replace("y",symbols["club"])
    elif "diamond" in card:
        return card_graph.replace("x",card[-1]).replace("y",symbols["diamond"])
    elif "heart" in card:
        return card_graph.replace("x",card[-1]).replace("y",symbols["heart"])
    elif "spade" in card:
        return card_graph.replace("x",card[-1]).replace("y",symbols["spade"])

def closed_card(i):
    return f"""{i}+---------+
{i}|         |
{i}|         |
{i}| CLOSED  |
{i}|         |
{i}|         |
{i}+---------+"""

def merge_graphics(cards):

    output=""
    try:
        for i in range(len(closed_card("").split("\n"))):
            for m in cards:
                output+=m.split("\n")[i]
            output+="\n"
        return output
    except:
        print(cards)
        