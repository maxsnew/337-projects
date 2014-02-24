from nominee import Nominee

# Award names have components, Motion Picture or Series
# actor/actrees
# 
class AwardName(object):
    def __init__(self, comps):
        self.components = comps
        
class Award(object):
    def __init__(self, name, noms):
        self.name = name
        self.nominees = noms
        self.winner = None
        
    def __repr__(self):
        return 'Award: Name=%s' % (self.name)

    def find_winner(self, tweets, fdist):
        """Find the winner of an award"""

        relevant = [ 
            t 
            for t in tweets
            if all([
                comp in t.rawtext
                for comp in self.name.components
            ])
            if t.is_win()
        ]
        # First, find the best words in this 
        if not (self.winner is None):
            return self.winner
        maxm = None
        winner = None

        for nom in self.nominees:
            curDist = fdist[nom.short_name(fdist)]
            if winner is None or curDist > maxm:
                maxm = curDist
                winner = nom

        self.winner = winner
        return winner

    def find_presenter(self, tweets, fdist):
        """Find the presenter of an award"""
        return None

# hard-coded, need to scrape!
awards = [ 
    Award(a_name, [Nominee(n_name) for n_name in ns])
    for (a_name, ns) in 
    [(AwardName(['Motion Picture', 'Drama']),
      ['Argo',
       'Django Unchained',
       'Life of Pi',
       'Lincoln',
       'Zero']),
     (AwardName(['Motion Picture', 'Musical', 'Comedy']), 
      ['Les Miserables', 
       'The Best Exotic Marigold Hotel',
       'Moonrise Kingdom',
       'Salmon Fishing in the Yemen',
       'Silver Linings Playbook']),
     (AwardName(['Actor', 'Motion Picture' 'Drama']),
      ['Daniel Day-Lewis',
       'Richard Gere',
       'John Hawkes',
       'Joaquin Phoenix',
       'Denzel Washington']),
      (AwardName(['Actress', 'Motion Picture', 'Drama']),
      ['Jessica Chastain',
       'Marion Cotillard', 
       'Helen Mirren', 
       'Naomi Watts',
       'Rachel Weisz'])
     # (u'Best Actor in a Motion Picture Musical or Comedy',
     #  ['Hugh Jackman',
     #   'Jack Black',
     #   'Bradley Copper',
     #   'Ewan McGregor',
     #   'Bill Murray']),
     # (u'Best Actress in a Motion Picture Musical or Comedy',
     #  ['Jennifer Lawrence',
     #   'Emily Blunt',
     #   'Judi Dench',
     #   'Maggie Smith',
     #   'Meryl Streep'] )
     # laziness
     # u'Best Actress in a Motion Picture Musical or Comedy',
     # u'Best Actress in a Television Comedy Series',
     # u'Best Mini-Series or Motion Picture made for Television',
     # u'Best Actor in a Mini-Series or Motion Picture made for Television',
     # u'Best Actress in a Mini-Series or Motion Picture made for Television',
     # u'Best Supporting Actor in a Series, Mini-Series or Motion Picture made for Television',
     # u'Best Supporting Actress in a Series, Mini-Series or Motion Picture made for Television',
     # u'Best Motion Picture Drama',
     # u'Best Motion Picture Musical or Comedy',
     # u'Best Director', 
     # u'Best Actor Motion Picture Drama',
     # u'Best Actor  Motion Picture Musical or Comedy',
     # u'Best Actress Motion Picture Drama',
     # u'Best Actress Motion Picture Musical or Comedy',
     # u'Best Supporting Actor Motion Picture', 
     # u'Best Supporting Actress Motion Picture',
     # u'Best Screenplay',
     # u'Best Original Score', 
     # u'Best Original Song',
     # u'Best Foreign Language Film',
     # u'Best Animated Feature Film '
 ] ]

# support_M = ['Christoph', 'Alan', 'Leonardo','Philip','Tommy']
# support_F = ['Anne','Amy','Sally','Helen','Nicole']
# director = ['Ben','Kathryn','Ang','Steven','Quentin']
# screenplay = ['Quentin','Chris','Tony','David','Mark']
# score = ['Mychael','Dario','Alexandre','John','Tom']
# song = ['Adele','Keith','Taylor','Claude']
# animated = ['Brave', 'Frankenweenie','Transylvania','Rise','Ralph']
# foreign = ['Amour','Royal','Intouchables','Tiki','Rust']
