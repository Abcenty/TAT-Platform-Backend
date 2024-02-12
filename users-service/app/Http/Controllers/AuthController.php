<?php

namespace App\Http\Controllers;

use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;
use Illuminate\Validation\ValidationException;

class AuthController extends Controller
{
    public function __construct()
    {
        $this->middleware('auth:api', ['except' => ['login']]);
    }

    /**
     * Авторизация пользователя
     *
     * @group Авторизация
     * @responseFile storage/responses/auth.login.json
     * @responseField access_token Bearer токен
     * @responseField expires_in Через сколько секунд токен станет неактивным
     */
    public function login(Request $request): JsonResponse
    {
        $credentials = $request->validate([
            'email' => 'required|email',
            'password' => 'required|string'
        ]);

        if(!$token = auth()->attempt($credentials)) {
            throw ValidationException::withMessages(['email' => __('auth.failed')]);
        }

        return response()->json([
            'access_token' => $token,
            'expires_in' => auth()->factory()->getTTL() * 60
        ]);
    }

    /**
     * Получение данных авторизованного пользователя
     *
     * @group Авторизация
     * @authenticated
     * @responseFile storage/responses/auth.me.json
     */
    public function me(): JsonResponse
    {
        return response()->json(auth()->user());
    }
}
