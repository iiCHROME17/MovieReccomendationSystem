import pandas as pd 
import os

class GenreList:
    def __init__(self, genre_dicts):
        # genre_dicts: list of dicts, e.g., [{'id': 35, 'name': 'Comedy'}]
        self.names = [d['name'] for d in genre_dicts if isinstance(d, dict) and 'name' in d]

    def __str__(self):
        return ', '.join(self.names)


class KeywordList:
    def __init__(self, keyword_dicts):
        # keyword_dicts: list of dicts, e.g., [{'id': 1, 'name': 'love'}]
        self.names = [d['name'] for d in keyword_dicts if isinstance(d, dict) and 'name' in d]

    def __str__(self):
        return ', '.join(self.names)

class DataProcessor:
    def __init__(self,path,version):
        """
        Path:       path (str): The file path to the CSV file.
        version:    version (int): The version of the data processor, default is 1 for movie data.
        """
        self.path = path
        self.df = None
        self.version = 1

    def load(self):
        """Load the CSV file into a DataFrame."""
        self.df = pd.read_csv(self.path)
        return self.df

    def drop_uneccessary_columns(self):
        """Drop unnecessary columns from the DataFrame."""
        if self.version == 1 and self.df is not None:
            cols_to_drop = [
                'budget',
                'homepage',
                'original_title',
                'popularity',
                'revenue',
                'status',
                'vote_average',
                'vote_count'
            ]
            self.df = self.df.drop(columns=[col for col in cols_to_drop if col in self.df.columns])

    def drop_nulls(self):
        """Drop rows with null values in the DataFrame."""
        if self.df is not None:
            self.df = self.df.dropna()

    def drop_duplicates(self):
        """If any duplicate IDs are found, drop the entire row."""
        if self.df is not None:
            self.df = self.df.drop_duplicates(subset=['id'], keep='first')
    
    def parse_json_fields(self, fields):
        """
        Parse JSON-like string fields (e.g., genres, keywords, cast, director) into Python objects (lists/dicts).
        Args:
            fields (list): List of column names to parse.
        """
        import ast
        if self.df is not None:
            for field in fields:
                if field in self.df.columns:
                    if field == 'genres':
                        self.df[field] = self.df[field].apply(
                            lambda x: GenreList(ast.literal_eval(x)) if pd.notnull(x) else GenreList([])
                        )
                    elif field == 'keywords':
                        self.df[field] = self.df[field].apply(
                            lambda x: KeywordList(ast.literal_eval(x)) if pd.notnull(x) else KeywordList([])
                        )
                    else:
                        self.df[field] = self.df[field].apply(lambda x: ast.literal_eval(x) if pd.notnull(x) else [])

    def save(self):
        """Save the processed DataFrame to the appropriate path based on version."""
        if self.version == 1 and self.df is not None:
            os.makedirs('data/modified', exist_ok=True)
            self.df.to_csv('data/modified/movies.csv', index=False)

    def extract_text_from_fields(self, fields, new_col='combined_text'):
        """
        Extract text from parsed fields and concatenate into a single string for each row.
        Args:
            fields (list): List of column names to extract text from.
            new_col (str): Name of the new column to store the combined text.
        """
        if self.df is not None:
            def extract_text(row):
                texts = []
                for field in fields:
                    if field in row and isinstance(row[field], list):
                        # For fields like genres/keywords/cast: list of dicts with 'name' key
                        texts.extend([d['name'] for d in row[field] if isinstance(d, dict) and 'name' in d])
                    elif field in row and isinstance(row[field], str):
                        texts.append(row[field])
                return ' '.join(texts)
            self.df[new_col] = self.df.apply(extract_text, axis=1)

class _DebugReader:
    """Private class for debugging: prints 5 different movies in readable English from the modified CSV."""
    def __init__(self, path='data/modified/movies.csv'):
        self.path = path
        self.df = pd.read_csv(self.path)

    def print_sample_movies(self, n=5):
        """Print a sample of movies in a readable format."""
        sample = self.df.sample(n=min(n, len(self.df)))
        for idx, row in sample.iterrows():
            print(f"\n--- Movie {idx+1} ---")
            print(f"Title: {row['title']}")
            print(f"Genres: {row['genres']}")
            print(f"Overview: {row['overview']}")
            print(f"Keywords: {row['keywords']}")
            print(f"Release Date: {row['release_date']}")
            print(f"Language: {row['original_language']}")
            print(f"Combined Text: {row['combined_text'][:120]}...")

def main():
    # Adjust the path and fields as needed
    processor = DataProcessor('data/raw/movies.csv', version=1)
    processor.load()
    processor.drop_uneccessary_columns()
    processor.drop_nulls()
    processor.drop_duplicates()
    # Specify the fields to parse as JSON-like
    json_fields = ['genres', 'keywords', 'cast', 'crew']
    processor.parse_json_fields(json_fields)
    # Extract text from relevant fields
    processor.extract_text_from_fields(['genres', 'keywords', 'cast', 'crew', 'overview'])
    processor.save()
    # Debugging: print sample movies
    debug_reader = _DebugReader()
    debug_reader.print_sample_movies()

if __name__ == "__main__":
    main()

        



