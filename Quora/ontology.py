#https://www.hackerrank.com/contests/quora-haqathon/challenges/ontology

from bisect import bisect_left
import re

def get_count(t, questions, topic, text):
    global counts

    c = counts.get((text, topic), -1)
    if c < 0:
        c = 0
        sentences = questions.get(topic, [])
        sentencesLen = len(sentences)
        textLen = len(text)
        
        idx = bisect_left(sentences, text, 0, sentencesLen)
        
        while idx < sentencesLen:
            c += 1 if sentences[idx].find(text) == 0 else 0
            if text < sentences[idx][:textLen]:
                break
            idx += 1

        for subtopic in t.get(topic, []):
            c += get_count(t, questions, subtopic, text)

        counts[(text, topic)] = counts.get((text, topic), 0) + c
        
    return c

N = int(raw_input())

t = {}
counts = {}
topics = raw_input()

m = re.findall(r"(\w+\s\(\s(\w+\s)+\))", topics)
while len(m) > 0:
#    print 'topics: ', topics
    for pattern in m:
        p = str(pattern[0])
        topics = topics.replace(p[p.find("("):p.find(")")+1], "")
        p = p.replace("(", " ")
        p = p.replace(")", " ")
        t[p[:p.find(" ")]] = p[p.find(" ")+1:].split()

    m = re.findall(r"(\w+\s+\(\s+(\w+\s+)+\))", topics)

#print t       

M = int(raw_input())

questions = {}

for i in xrange(M):
    (topic, question) = raw_input().split(': ')
    l = questions.get(topic, [])
    l.append(question)
    questions[topic] = l

for category in questions:
    questions[category].sort()

#print questions
K = int(raw_input())

for i in xrange(K):
    query = raw_input()
    query_topic = query[:query.index(" ")]
    query_text = query[query.index(" ")+1:]

    res = get_count(t, questions, query_topic, query_text)
    print res
#    print query_topic, query_text

