import { Box, SimpleGrid, Heading } from '@chakra-ui/react';
import MovieCard from './components/MovieCard';

// Example movie data (replace with real data or fetch from backend)
const movies = [
  { title: 'Avatar' },
  { title: 'Inception' },
  { title: 'The Dark Knight' },
  { title: 'Interstellar' },
  { title: 'The Matrix' },
  // ...add more or map from your data
];

function App() {
  return (
    <Box bg="gray.900" minH="100vh" p={8}>
      <Heading color="red.500" mb={8} textAlign="center" fontFamily="sans-serif">
        iWatchMovies
      </Heading>
      <SimpleGrid columns={[1, 2, 3, 5]} spacing={6}>
        {movies.map((movie, idx) => (
          <MovieCard key={idx} title={movie.title} />
        ))}
      </SimpleGrid>
    </Box>
  );
}

export default App;
