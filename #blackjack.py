#blackjack
import random
t1 = 0
t2 = 0
tp1 = 0
crd1 = 'f'
crn1 = 'f'
tp2 = 0
crd2 = 'f'
crn2 = 'f'
counter = 0
st = 'f'
for times in range (0,2) :
    tp1 = random.randrange(1,5)
    tp2 = random.randrange(1,5)

    if tp1 == 1 :
        crd1 = 'Clubs'
    if tp1 == 2 :
        crd1 = 'Diamonds'
    if tp1 == 3 :
        crd1 = 'Hearts'
    if tp1 == 4 :
        crd1 = 'Spades'

    if tp2 == 1 :
        crd2 = 'Clubs'
    if tp2 == 2 :
        crd2 = 'Diamonds'
    if tp2 == 3 :
        crd2 = 'Hearts'
    if tp2 == 4 :
        crd2 = 'Spades'

    crn1 = random.randrange(0,14)
    crn2 = random.randrange(0,14)
    
    if 0 < crn1 < 11 :
        crnt1 = crn1
    elif crn1 == 0 :
        crnt1 = 'Ace'
    elif crn1 == 11 :
        crnt1 = 'King'
    elif crn1 == 12 :
        crnt1 = 'Queen'
    elif crn1 == 13 :
        crnt1 = 'Joker'
    
    if 0 < crn2 < 11 :
        crnt2 = crn2
    elif crn2 == 0 :
        crnt2 = 'Ace'
    elif crn2 == 11 :
        crnt2 = 'King'
    elif crn2 == 12 :
        crnt2 = 'Queen'
    elif crn2 == 13 :
        crnt2 = 'Joker'
    
    
    if crn1 == 11 or crn1 == 12 or crn1 == 13 :
        t1 += 10
    elif crn1 == 0 :
        if t1 > 10 :
            t1 += 1
        else : 
            crn1 = 11
            t1 += crn1
    else : t1 += crn1

    if crn2 == 11 or crn2 == 12 or crn2 == 13 :
        t2 += 10
    elif crn2 == 0 :
        if t2 > 10 :
            t2 += 1
        else : 
            t2 += 11
    else : t2 += crn2

    print ('P1 , Cards dealt:' , crnt1 , 'of' , crd1)
    
    print ('P2 , Cards dealt:' , crnt2 , 'of' , crd2)
    
print ('P1:' , t1)
print ('P2:' , t2)
if t1 == 21 :
    print ('Blackcack. Player 1 wins!')
if t2 == 21 :
    print ('Blackcack. Player 2 wins!')

while t1 < 21 and t2 < 21 :
    if (counter % 2) == 0 :
        st = input('(Hit/Stand): ')
        if  st == 'h' or st == 'hit' or st == 'H' or st == 'Hit' :
            tp1 = random.randrange(1,5)
            if tp1 == 1 :
                crd1 = 'Clubs'
            if tp1 == 2 :
                crd1 = 'Diamonds'
            if tp1 == 3 :
                crd1 = 'Hearts'
            if tp1 == 4 :
                crd1 = 'Spades'
            crn1 = random.randrange(0,14)
            
            if 0 < crn1 < 11 :
                crnt1 = crn1
            elif crn1 == 0 :
                crnt1 = 'Ace'
            elif crn1 == 11 :
                crnt1 = 'King'
            elif crn1 == 12 :
                crnt1 = 'Queen'
            elif crn1 == 13 :
                crnt1 = 'Joker'
            
            if crn1 == 11 or crn1 == 12 or crn1 == 13 :
                t1 += 10
            elif crn1 == 0 :
                if t1 > 10 :
                    t1 += 1
                else : 
                    crn1 = 11
                    t1 += crn1
            else : t1 += crn1
            if st == 'h' or 'hit' or 'H' or 'Hit' :
                print ('Dealt card:' , crnt1 , 'of' , crd1)
            
    else :
        st = input('(Hit/Stand): ')
        if  st == 'h' or st == 'hit' or st == 'H' or st == 'Hit' :
            tp2 = random.randrange(1,5)
            if tp2 == 1 :
                crd2 = 'Clubs'
            if tp2 == 2 :
                crd2 = 'Diamonds'
            if tp2 == 3 :
                crd2 = 'Hearts'
            if tp2 == 4 :
                crd2 = 'Spades'
            crn2 = random.randrange(0,14)
            
            if 0 < crn2 < 11 :
                crnt2 = crn2
            elif crn2 == 0 :
                crnt2 = 'Ace'
            elif crn2 == 11 :
                crnt2 = 'King'
            elif crn2 == 12 :
                crnt2 = 'Queen'
            elif crn2 == 13 :
                crnt2 = 'Joker'

            if crn2 == 11 or crn2 == 12 or crn2 == 13 :
                t1 += 10
            elif crn2 == 0 :
                if t2 > 10 :
                    t2 += 1
                else : 
                    t2 += 11
            else : t2 += crn2
            
            if st == 'h' or 'hit' or 'H' or 'Hit' :
                print ('Dealt card:' , crnt2 , 'of' , crd2)
    
    counter += 1
    print ('P1:' , t1)
    print ('P2:' , t2)

if t1 == 21 :
    print ('Player 1 wins!')
if t2 == 21 :
    print ('Player 2 wins!')
if t1 > 21 :
    print ('Player 1 busted.')
if t2 > 21 :
    print ('Player 2 busted.')

if t1 == t2 or (t1 > 21 and t2 > 21) :
    print ('Draw')

#will be adding the dealer with the hole card soon