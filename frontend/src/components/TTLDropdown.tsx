import React, { FC } from 'react';
import styled from 'styled-components';

export const TTLDropdown: FC = () => {
  const StyledSelect = styled.select`
    margin-left: 0.01em;
  `;

  return (
    <>
      <label ></label>
      <StyledSelect name="ttl" id="ttl-select-dropdown">
        <option value="one-day">One Day</option>
        <option value="one-week">One Week</option>
        <option value="one-month">One Month</option>
      </StyledSelect>
    </>
  );
};
