from nominee import Nominee

# Award names have components, Motion Picture or Series
# actor/actrees
# 
class AwardName(object):
    def __init__(self, comps):
        self.components = comps

    def __repr__(self):
        return ' '.join(['Best'] + self.components)
        
class Award(object):
    def __init__(self, name, noms):
        self.name = name
        self.nominees = noms
        self.winner = None
        
    def __repr__(self):
        return 'Award: Name=%s' % (self.name)

    def find_winner(self, tweets):
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
        maxm = None
        winner = None

        for nom in self.nominees:
            curCount = len([
                t for t in relevant if nom.name in t.rawtext
            ])
            if maxm is None or curCount > maxm:
                maxm = curCount
                winner = nom

        self.winner = winner
        return winner

    def find_presenter(self, tweets):
        """Find the presenter of an award"""
        return None

# hard-coded, need to scrape!
awards = [ 
    Award(a_name, [Nominee(n_name) for n_name in ns])
    for (a_name, ns) in 
    [(AwardName(['Motion Picture', 'Drama']),
      ['Django Unchained',
       'Zero Dark Thirty',
       'Argo',
       'Life of Pi',
       'Lincoln'
       ]),
     (AwardName(['Motion Picture', 'Musical', 'Comedy']), 
      ['Les Miserables', 
       'The Best Exotic Marigold Hotel',
       'Moonrise Kingdom',
       'Salmon Fishing in the Yemen',
       'Silver Linings Playbook']),
     (AwardName(['Actor', 'Motion Picture', 'Drama']),
      ['Joaquin Phoenix',
       'John Hawkes',
       'Daniel Day-Lewis',
       'Richard Gere',
       'Denzel Washington']),
      (AwardName(['Actress', 'Motion Picture', 'Drama']),
       ['Marion Cotillard', 
        'Helen Mirren', 
        'Jessica Chastain',
        'Naomi Watts',
        'Rachel Weisz']),
     (AwardName(['Actor',
                 'Motion Picture',
                 'Musical',
                 'Comedy']),
      ['Hugh Jackman',
       'Jack Black',
       'Bradley Copper',
       'Ewan McGregor',
       'Bill Murray']),
     (AwardName(['Actress', 'Motion Picture', 'Musical', 'Comedy']),
      ['Jennifer Lawrence',
       'Emily Blunt',
       'Judi Dench',
       'Maggie Smith',
       'Meryl Streep']),
     (AwardName(['Supporting Actor', 'Motion Picture','Drama','Musical','Comedy']),
      ['Christoph Waltz',
      'Alan Arkin',
      'Leonardo DiCaprio',
      'Philip Seymour Hoffman',
      'Tommy Lee Jones']),
     (AwardName(['Supporting Actress', 'Motion Picture','Drama','Musical','Comedy']),
      ['Anne Hathaway',
      'Amy Adams',
      'Sally Field',
      'Helen Hunt',
      'Nicole Kidman']),
     (AwardName(['Director']),
      ['Ben Affleck',
      'Kathryn Bigelow',
      'Ang Lee',
      'Steven Spielberg',
      'Quentin Tarantino']),
     (AwardName(['Screenplay']),
      ['Quentin Tarantino',
      'Chris Terrio',
      'Tony Kushner',
      'David O. Russell',
      'Mark Boal']),
     (AwardName(['Original Score']),
      ['Mychael Danna',
      'Dario Marianelli',
      'Alexandre Desplat',
      'John Williams',
      'Tom Tykwer, Johnny Klimek & Reinhold Heil']),
     (AwardName(['Original Song']),
      ['Skyfall',
      'For You',
      'Not Running Anymore',
      'Safe & Sound',
      'Suddenly']),
     (AwardName(['Animated']),
      ['Brave',
      'Frankenweenie',
      'Hotel Transylvania',
      'Rise of the Guardians',
      'Wreck-It Ralph']),
     (AwardName(['Foreign']),
      ['Amour',
      'A Royal Affair',
      'The Intouchables',
      'Kon-Tiki',
      'Rust and Bone']),
     (AwardName(['Series','Drama']),
      ['Homeland',
      'Breaking Bad',
      'Boardwalk Empire',
      'Downton Abbey',
      'The Newsroom']),
     (AwardName(['Series','Musical','Comedy']),
      ['Girls',
      'The Big Bang Theory',
      'Episodes',
      'Modern Family',
      'Smash']),
     (AwardName(['Actor','Series','Drama']),
      ['Damien Lewis',
      'Steve Buscemi',
      'Bryan Cranston',
      'Jeff Daniels',
      'Jon Hamm']),
     (AwardName(['Actress','Series','Drama']),
      ['Claire Danes',
      'Connie Britton',
      'Glenn Close',
      'Michelle Dockery',
      'Julianna Margulies']),
     (AwardName(['Actor','Series','Comedy']),
      ['Don Cheadle',
      'Alec Baldwin',
      'Louis C.K.',
      'Matt LeBlanc',
      'Jim Parsons']),
     (AwardName(['Actress','Series','Comedy']),
      ['Lena Dunham',
      'Zooey Deschanel',
      'Tina Fey',
      'Julia Louis-Dreyfus',
      'Amy Poehler']),
     (AwardName(['Actor','Miniseries']),
      ['Ed Harris',
      'Max Greenfield',
      'Danny Huston',
      'Mandy Patinkin',
      'Eric Stonestreet']),
     (AwardName(['Actress','Miniseries']),
      ['Maggie Smith',
      'Hayden Panettiere',
      'Archie Panjabi',
      'Sarah Paulson',
      'Sofia Vergara']),
     (AwardName(['Best','Miniseries']),
      ['Game Change',
      'The Girl',
      'The Hour',
      'Hatfields & McCoys',
      'Political Animals'])
 ] ]
