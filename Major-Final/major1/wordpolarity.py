import Algorithmia

def somefunction(input):
    client = Algorithmia.client('simL4K0sq9xovn9rSUqxzGy19R/1')
    algo = client.algo('mtman/SentimentAnalysis/0.1.1')
    ans = algo.pipe(input).result
    return ans

