class Alternative:

    other_annual_costs = None

    def __init__(self, name, service_life, initial_cost, annual_maintenance_cost, salvage_value, other_annual_costs = None):

        """ 
            define inputs
            name is a string
            service life is a integer
            initial cost, annual maintenance cost, and salvage value are floats
            other annual costs is a dictionary that associates a string cost name to a cost that is a float 
            
        """

        self.name = name
        self.service_life = service_life
        self.initial_cost = initial_cost
        self.annual_maintenance_cost = annual_maintenance_cost
        self.salvage_value = salvage_value

        # make sure that there are actually other annual costs

        if other_annual_costs is not None:

            self.other_annual_costs = other_annual_costs

    def __str__(self):

        """ 

            prints a list of inputs 
            
        """
        
        alt = 'Alternative: {}\nService Life: {} years\n'.format(self.name, self.service_life)

        # round cost to two decimal places

        init_cost = round(self.initial_cost, 2) 
        ann_main_cost = round(self.annual_maintenance_cost, 2)
        salv_val = round(self.salvage_value, 2)

        alt += 'Initial Cost: ${}\n'.format('{0:,}'.format(init_cost))
        alt += 'Annual Maintenance Cost: ${}\n'.format('{0:,}'.format(ann_main_cost))
        alt += 'Salvage Value: ${}\n'.format('{0:,}'.format(salv_val))
        
        # check to see if there are other annual costs

        if self.other_annual_costs is not None:

            for item in self.other_annual_costs:
                
                other_cost = round(self.other_annual_costs[item], 2)

                alt += item + ': ${}\n'.format('{0:,}'.format(other_cost))

        return alt

class Economic_Analysis:
    
    def __init__(self, alternatives, interest_rate):

        """ 
            define inputs
            alternatives is a list of Alternative objects
            interest rate is a decimal

        """

        self.alternatives = alternatives
        self.interest_rate = interest_rate
    
    def __str__(self):

        """
            
            lists the number of alternatives being analyzed
        
        """

        alt_str = 'Alternatives Analyzed:' + str(len(self.alternatives)) + '\n'

        # lists the alternatives by number

        count = 1

        for alt in self.alternatives:

            alt_str += str(count) + ': ' + alt.name + '\n'
            count += 1

        return alt_str    

    def SPPWF(self, years):

        """

            SPPWF stands for singe payment present worth factor
            given future amount, find present amount
        
        """

        return 1/self.SPCAF(years)
    
    def SPCAF(self, years):

        """

            SPCAF stands for single payment compound amount factor
            given present amount, find future amount
        
        """

        return (1+self.interest_rate)**years
    
    def CRF(self, years):
        
        """

            CRF stands for capital recovery factor
            given present amount, find annual ammount

        """
        return 1/self.USPWF(years)

    def USPWF(self, years):
        
        """

            USPWF stands for uniform series present worth factor
            given annual amount, find present amount

        """
        return (self.SPCAF(years) - 1)/(self.interest_rate * self.SPCAF(years))

    def USCAF(self, years):
        
        """

            USCAF stands for uniform series compound amount factor
            given annual amount, find future amount

        """
        return 1/self.USSFF(years)

    def USSFF(self, years):

        """

            USSFF stands for uniform series sinking fund factor
            given future amount, find annual amount
        
        """

        return self.interest_rate/(self.SPCAF(years) - 1)
    
    def present_worth(self, alt):

        """

            finds the present worth of an alternative
            alt is an Alternative object
        
        """

        # use factors to move costs to present time

        pworth = alt.initial_cost + (alt.annual_maintenance_cost * self.USPWF(alt.service_life)) - (alt.salvage_value * self.SPPWF(alt.service_life))
            
        # find present worth of other annual costs if it exists

        if alt.other_annual_costs is not None:

            for other in alt.other_annual_costs:

                pworth += (alt.other_annual_costs[other] * self.USPWF(self.alt.service_life))

        return pworth

    def present_worth_method(self):

        """
            present worth method is an economic analysis technique 
            chooses the best alternative based on the lowest cost 
            and assumes that all alternatives have the same benefits
            ** only works if the alternatives have the same service life **

        """
        
        # loop through alternatives and find present worth for each and store into a dictionary

        pworths = {}

        for alt in self.alternatives:
            
            pworth = self.present_worth(alt)

            pworths[alt.name] = pworth

        # find lowest present worth by looping through pworths
        # initially assume the first alternative is the best

        best_alternative = pworths.keys()[0]
        lowest_cost = pworths[pworths.keys()[0]]

        for cost in pworths:

            if pworths[cost] < lowest_cost:

                lowest_cost = pworths[cost]
                best_alternative = cost
        
        lowest_cost = round(lowest_cost, 2)

        return 'Best Alternative: {}\nCost: ${}'.format(best_alternative, '{0:,}'.format(lowest_cost))

    def annual_cost(self, alt):

        """

            finds the annual cost of an alternative
            alt is an alternative object
        
        """

        # use different factors to annualize costs

        aworth = (alt.initial_cost * self.CRF(alt.service_life)) + alt.annual_maintenance_cost - (alt.salvage_value * self.USSFF(alt.service_life)) 

        # loops through other annual costs and adds them to aworth

        if alt.other_annual_costs is not None: 

            for cost in alt.other_annual_costs:

                aworth += alt.other_annual_costs[cost]

        return aworth

    def annual_cost_method(self):

        """
            chooses the best alternative based on all the costs converted to annual form 
            and assumes that all alternatives have the same benefits

        """
        aworths = {}

        # loops through alternatives and finds the total annual costs

        for alt in self.alternatives:
            
            aworth = self.annual_cost(alt)

            aworths[alt.name] = aworth

        # assume that the best alternative is the first one

        best_alternative = aworths.keys()[0]
        lowest_cost = aworths[aworths.keys()[0]]

        # find lowest present worth by looping through aworths

        for cost in aworths:

            if aworths[cost] < lowest_cost:

                lowest_cost = aworths[cost]
                best_alternative = cost
        
        lowest_cost = round(lowest_cost, 2)

        return 'Best Alternative: {}\nCost: ${}'.format(best_alternative, '{0:,}'.format(lowest_cost))

    def benefit_cost_method(self, highway_user_costs):

        """

            chooses the best alternative by using an algorithm that compares 
            the benefits of two alternatives
            highway user costs is a dictionary that associates the alternative name 
            to the the annual highway user costs 
        
        """

        # if the first alternative is the null alternative, which does not implement anything

        if self.alternatives[0].name == 'Null':
            
            alt_highway_costs = self.annual_cost(self.alternatives[1])

            BC_ratio = (highway_user_costs['Null'] - highway_user_costs[self.alternatives[1].name]) / alt_highway_costs

            if BC_ratio > 1:
                
                print('BC Ratio: ' + str(round(BC_ratio, 2)))    

                return 'Best Alternative: {}'.format(self.alternatives[1].name)

            else:

                return 'Best Alternative: Null Alternative'

        
        # if the second alternative is the null alternative

        elif self.alternatives[1].name == 'Null':

            alt_highway_costs = self.annual_cost(self.alternatives[0])

            BC_ratio = (highway_user_costs['Null'] - highway_user_costs[self.alternatives[0].name]) / alt_highway_costs

            if BC_ratio > 1:

                print('BC Ratio: ' + str(round(BC_ratio, 2)))   

                return 'Best Alternative: {}'.format(self.alternatives[0].name)
            
            else:

                return 'Best Alternative: Null Alternative'
    
        # if neither are the null alternative

        else:
            
            alt_highway_costs1 = self.annual_cost(self.alternatives[0])

            alt_highway_costs2 = self.annual_cost(self.alternatives[1])

            if alt_highway_costs1 < alt_highway_costs2:

                BC_ratio = (highway_user_costs[self.alternatives[0].name] - highway_user_costs[self.alternatives[1].name]) / (alt_highway_costs2 - alt_highway_costs1)

                if BC_ratio > 1:
                    
                    print('BC Ratio: ' + str(round(BC_ratio, 2)))

                    return 'Best Alternative: {}'.format(self.alternatives[1].name)

            elif alt_highway_costs1 > alt_highway_costs2:

                BC_ratio = (highway_user_costs[self.alternatives[1].name] - highway_user_costs[self.alternatives[0].name]) / (alt_highway_costs1 - alt_highway_costs2)

                if BC_ratio > 1:
                    
                    print('BC Ratio: ' + str(round(BC_ratio, 2)))

                    return 'Best Alternative: {}'.format(self.alternatives[0].name)
      
