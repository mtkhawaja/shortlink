import React, { useState } from 'react';
import { BACKEND_URL, BASE_URL } from '../config/settings';
import { useForm } from 'react-hook-form';
import { Form, Button, InputGroup, FormControl } from 'react-bootstrap';

interface IURLConfig {
  setOriginalURL: React.Dispatch<React.SetStateAction<string>>;
  setShortlink: React.Dispatch<React.SetStateAction<string>>;
}

export function URLForm(props: IURLConfig) {
  const { register, handleSubmit } = useForm();
  const { setOriginalURL, setShortlink } = props;
  const onSubmit = async (data: any) => {
    const endpoint = `${BACKEND_URL}/shortlink`;
    const postData = {
      original_url: data['original_url'],
    };
    const response = await fetch(endpoint, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      referrerPolicy: 'no-referrer',
      body: JSON.stringify(postData),
    });
    const jsonResponse = await response.json();
    setOriginalURL(data['original_url']);
    setShortlink(`${BASE_URL}/${jsonResponse['key_str']}`);
  };

  return (
    <>
      <Form onSubmit={handleSubmit(onSubmit)}>
        <FormControl
          className="text-center rounded"
          name="original_url"
          defaultValue=""
          placeholder="https://example.com"
          ref={register({ required: true })}
          type="url"
        />
        <InputGroup className="p-3 d-block text-center">
          <label htmlFor="url-lifetime-options">URL lifetime:</label>
          <select
            id="url-lifetime-options"
            className="ml-2"
            name="url-lifetime-options"
          >
            <option value="hour">1 Hour</option>
            <option value="day">1 Day</option>
            <option value="week">1 Week</option>
            <option value="month">1 Month</option>
          </select>
        </InputGroup>

        <div className="text-center">
          <Button className="btn-dark" type="submit">
            Submit
          </Button>
        </div>
      </Form>
    </>
  );
}
