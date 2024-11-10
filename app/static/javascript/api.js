function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          // Verifica se o cookie começa com o nome que queremos
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}

async function getProductList() {
  const response = await fetch('/v1/product/');
  return response.json();
}

async function getProduct(id) {
    const response = await fetch(`/v1/product/${id}`);
    return response.json();
}

async function createProduct(product) {
  const response = await fetch('/v1/product/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(product),
  });
  return response.json();
}

async function updateProduct(id, product) {
    const response = await fetch(`/v1/product/${id}`, {
        method: 'PUT',
        headers: {
        'Content-Type': 'application/json',
        },
        body: JSON.stringify(product),
    });
    return response.json();
}

async function deleteProduct(id) {
    const response = await fetch(`/v1/product/${id}`, {
        method: 'DELETE',
    });
    return response.json();
}

async function getCartList() {
  const response = await fetch('/v1/cart/');
  return response.json();
}

async function finishCart(form){
  const response = await fetch('/v1/cart/finish_cart/', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': getCookie('csrftoken'),
      },
      body: JSON.stringify(form),
  });

  if (!response.ok) {
      return null;
  }

  return response.json();
}

