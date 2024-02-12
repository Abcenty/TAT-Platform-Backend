<?php

namespace App\Http\Controllers;

use App\Http\Resources\UserCollection;
use App\Models\User;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;
use Illuminate\Pagination\LengthAwarePaginator;
use Illuminate\Support\Facades\Hash;
use Illuminate\Validation\Rules;

class UserController extends Controller
{
    /**
     * Получение списка зарегистрированных пользователей
     *
     * @group Пользователи
     *
     * @apiResourceModel App\Models\User paginate=10
     */
    public function index(Request $request)
    {
        $request->validate([
            'page' => 'integer',
            'limit' => 'integer|min:1|max:100'
        ]);
        return User::paginate($request->input('limit', 10));
    }

    /**
     * Добавление нового пользователя
     *
     * @group Пользователи
     */
    public function store(Request $request): User
    {
        $request->validate([
            'last_name' => ['required', 'string', 'max:255'],
            'first_name' => ['required', 'string', 'max:255'],
            'patronymic' => ['string', 'max:255'],
            'email' => ['required', 'string', 'lowercase', 'email', 'max:255', 'unique:'.User::class],
            'password' => ['required', 'min:8', Rules\Password::defaults()],
        ]);

        return User::create([
            'last_name' => $request->last_name,
            'first_name' => $request->first_name,
            'patronymic' => $request->patronymic,
            'email' => $request->email,
            'password' => Hash::make($request->password),
        ]);
    }

    /**
     * Получение данных пользователя
     *
     * @group Пользователи
     */
    public function show($id)
    {
        $userId = (int) $id;

        $user = User::find($userId);

        if (!$user) {
            abort(404, 'Пользователь не найден');
        }

        return $user;
    }

    /**
     * Изменение данных пользователя
     *
     * @group Пользователи
     */
    public function update(Request $request, User $user): User
    {
        $request->validate([
            'last_name' => ['string', 'min:1', 'max:255'],
            'first_name' => ['string', 'min:1', 'max:255'],
            'patronymic' => ['string', 'max:255'],
            'email' => ['string', 'lowercase', 'email', 'max:255', 'unique:'.User::class.',email,'.$user->id],
            'password' => ['nullable', 'min:8', Rules\Password::defaults()],
        ]);

        $user->update([
            'last_name' => $request->last_name ?? $user->last_name,
            'first_name' => $request->first_name ?? $user->first_name,
            'patronymic' => $request->patronymic ?? $user->patronymic,
            'email' => $request->email ?? $user->email,
            'password' => $request->password ? Hash::make($request->password) : $user->password,
        ]);

        return $user;
    }

    /**
     * Удаление пользователя
     *
     * @group Пользователи
     */
    public function destroy(User $user): JsonResponse
    {
        $user->delete();
        return response()->json(['message' => 'Пользователь удалён']);
    }
}
