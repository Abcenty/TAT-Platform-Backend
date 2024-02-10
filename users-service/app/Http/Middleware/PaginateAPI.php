<?php

namespace App\Http\Middleware;

use Closure;
use Illuminate\Http\Request;
use Symfony\Component\HttpFoundation\Response;

class PaginateAPI
{
    public function handle(Request $request, Closure $next): Response
    {
        $response = $next($request);

        $data = $response->getData(true);

        $keys = ['links', 'first_page_url', 'last_page_url', 'next_page_url', 'prev_page_url', 'path'];

        foreach ($keys as $key) {
            unset($data[$key]);
        }

        $response->setData($data);

        return $response;
    }
}
