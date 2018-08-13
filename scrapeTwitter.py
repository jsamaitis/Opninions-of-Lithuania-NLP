import twint

class scrapeTweets:
    '''
    Documented, watered down version of twint.
    
    Returns None.
    ------
    Parameters, attributes or whatever:
    
    since (str): date to start searching from.
    
    until (str): date to end the search on.
    
    language (str): get tweets which are written in a specific language only. (Doesn't work 100% correctly in classifying).
    
    store_csv (bool): if true, saves a csv file.
    
    csv_fieldnames (list of (str)): parameters to include in csv file. Further info in twint's GitHub.
    
    csv_output (str): filename of output file.
    
    '''
    def __init__(
        self,
        search,
        since = None,
        until = None,
        language = 'en',
        store_csv = True,
        csv_fieldnames = ["id", "user_id", "username", "date", "time", "timezone", "tweet", "replies", "retweets", "likes"],
        csv_output = 'twitter_data.csv'):
    
        self.term = search
        self.since = since
        self.until = until
        self.lang = language
        self.store = store_csv
        self.csv_fn = csv_fieldnames
        self.out = csv_output
        self.search()
        
    def search(self):
        '''
        Executes twint with parameters specified in the class.
        
        Returns None.
        ------
        Parameters:
        
        None
        '''
        # Configure base parameters.
        c = twint.Config()
        c.Search = self.term
        if self.since != None:
            c.Since = self.since
        if self.until != None:
            c.Until = self.until
        c.Lang = self.lang
        
        # Configure storing.
        c.Store_csv = self.store
        c.Custom = self.csv_fn
        c.Output = self.out
        
        # Run the scraper.
        twint.run.Search(c)
        
        return None
    
scrapeTweets(search='lithuania') # Can be deleted if you want to import it as a class. 