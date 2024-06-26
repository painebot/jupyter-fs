/******************************************************************************
 *
 * Copyright (c) 2019, the jupyter-fs authors.
 *
 * This file is part of the jupyter-fs library, distributed under the terms of
 * the Apache License 2.0.  The full license can be found in the LICENSE file.
 *
 */
import "isomorphic-fetch";

import { browser, progressStatus } from "../src/index";

describe("Checks activate", () => {
  test("Check activate", () => {
    expect(browser.activate);
    expect(progressStatus);
  });
});
