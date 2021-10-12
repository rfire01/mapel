#!/usr/bin/env python

class Family:
    """ Family of elections: a set of elections from the same election model """

    def __init__(self, model="none", family_id='none', params=None, size=1, label="none",
                 color="black", alpha=1., show=True, marker='o', starting_from=0,
                 num_candidates=None, num_voters=None, single_election=False,
                 election_ids=None, ballot='ordinal', path=None, num_nodes=None):

        self.family_id = family_id
        self.model = model
        self.params = params
        self.size = size
        self.label = label
        self.color = color
        self.alpha = alpha
        self.show = show
        self.marker = marker
        self.starting_from = starting_from
        self.num_candidates = num_candidates
        self.num_voters = num_voters
        self.single_election = single_election
        self.election_ids = election_ids
        self.ballot = ballot
        self.path = path
        self.num_nodes = num_nodes

# # # # # # # # # # # # # # # #
# LAST CLEANUP ON: 12.10.2021 #
# # # # # # # # # # # # # # # #
