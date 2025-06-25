import { Box, Text } from '@chakra-ui/react';

export default function MovieCard({ title }) {
  return (
    <Box
      bg="gray.800"
      color="white"
      borderRadius="lg"
      boxShadow="lg"
      p={6}
      m={2}
      minW="200px"
      minH="120px"
      display="flex"
      alignItems="center"
      justifyContent="center"
      fontSize="xl"
      fontWeight="bold"
      transition="transform 0.2s"
      _hover={{
        transform: 'scale(1.08)',
        zIndex: 1,
        boxShadow: '2xl',
        cursor: 'pointer',
      }}
    >
      <Text textAlign="center">{title}</Text>
    </Box>
  );
}
