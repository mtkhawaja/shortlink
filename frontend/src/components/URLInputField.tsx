import React, { FC } from 'react';
import { Button, InputGroup, FormControl } from 'react-bootstrap';
import { TTLDropdown } from './TTLDropdown';
export const URLInputField: FC = () => {
  return (
    <>
      <InputGroup>
        <FormControl
          className="text-center"
          placeholder="https://example.com/"
          aria-label="Input field for URL to shorten."
        />
        <TTLDropdown />
      </InputGroup>
      <div className="text-center pt-3">
        <Button variant="dark"> Shorten </Button>
      </div>
    </>
  );
};
