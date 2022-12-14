import * as React from "react";
import {
  ChakraProvider,
  Box,
  Text,
  Link,
  VStack,
  Code,
  Grid,
  theme,
} from "@chakra-ui/react";
import { ColorModeSwitcher } from "./ColorModeSwitcher";
import { Logo } from "./Logo";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import routes from "./routes";
import { Home } from "./pages/Home";
import { Movie } from "./pages/Movie";
import { TheaterPage } from "./pages/Theater";

export const App = () => (
  <ChakraProvider theme={theme}>
    <BrowserRouter>
      <Routes>
        <Route path={routes.home} element={<Home />} />
        <Route path={routes.theater} element={<TheaterPage />} />
        <Route path={routes.movie} element={<Movie />} />
      </Routes>
    </BrowserRouter>
  </ChakraProvider>
);
