P_spam = 0.25
P_offer_given_spam = 0.80
P_offer_given_notspam = 0.10

P_notspam = 1 - P_spam

P_offer = (P_offer_given_spam * P_spam) + \
          (P_offer_given_notspam * P_notspam)

P_spam_given_offer = (P_offer_given_spam * P_spam) / P_offer

print("Probability Email is Spam given Offer =",
      P_spam_given_offer)

print("\nInterpretation:")
print("Emails containing 'Offer' are much more likely to be spam.")